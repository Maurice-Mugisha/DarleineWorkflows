<?php


if(isset($_GET['specific_workflow'])):


	$workflow_id = isset($_GET['workflow_id']) ? $fieldValidator->validate_field($_GET['workflow_id']) : "";

	$workflowstepmap_array = array();
	$step_array = array();
	$workflow_array = array();

	$query = $queryExecutor->execute($selectionObj->select_workflow($workflow_id));

	while($row = mysqli_fetch_array($query)):

		$workflow_id = $row['workflow_id'];
		$workflow_array[$workflow_id] = array();
		$workflow_array[$workflow_id]['workflow_id'] = $workflow_id;		$workspace_id = $row['workspace_id'];
		$workflow_array[$workspace_id] = array();
		$workflow_array[$workspace_id]['workspace_id'] = $workspace_id;

		$key = $workflow_id.$workspace_id.;


		$secondary_query = $queryExecutor->execute($selectionObj->select_workflowstepmap_by_workflow($workflow_id));

		while($sec_row = mysqli_fetch_array($secondary_query)):

			$step_id = $sec_row['step_id'];
			$step_array[$step_id] = array();
			$step_array[$step_id]['step_id'] = $step_id;

			$sec_key = $step_id;

			$dependent_query = $queryExecutor->execute($selectionObj->select_step($step_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$step_array[$sec_key]['name'] = $row_col['name'];

		endwhile;



	endwhile;


?>

<table cellspacing = "1" cellpadding = "0" align = "center" width = "100%" id = "workflowstepmap">
 <tr>
 <td colspan = "2">&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td colspan = "2"><a href="target_print.php?workflowstepmap&&workflow_id=<?= $workflow_id ?>" target="_blank" style="color:#00FF00;">Print PDF</a></td></tr>
 <tr class = "top_row">
 <td>&nbsp;&nbsp;#&nbsp;&nbsp;</td>
 <td>&nbsp;Step id&nbsp;</td>
 <td>&nbsp;Name&nbsp;</td>
 <td>&nbsp;&nbsp;Actions&nbsp;&nbsp;</td></tr>
 
<?php $i = 0; ?>


<?php  foreach($step_array as $step_key => $step_value): ?>
<?php $css_class = ($i+1)%2 == 0 ? "even_row" : "odd_row"; ?>


<tr>
	<td><?= ($i+1) ?></td>
	<td><?= $step_value['step_id'] ?></td>
	<td><?= $step_value['name'] ?></td>
	<td>

		<?php $id_string = $step_id; ?>

		<div id="update_step_<?= $id_string ?>" style="display:none" class="updates">
		<table border="0" align="center" class="overlay_contained_table">
		<tr>
			<td align="right">
			<div class="closebtn" id="close_circle" onclick="closeUpdateOverlay('update_step_<?= $id_string ?>');">&nbsp;&times;&nbsp;</div>
			</td>
		</tr>
		<tr><td><br /></td></tr>
		<tr>
			<td align="center">
			<fieldset style="width: 80%">
			<legend>step Information</legend>
			<?php update_step($queryExecutor, $selectionObj, $updateObj, $fieldValidator, $step_value['step_id']); ?>
			</fieldset>
			</td>
		</tr>
		<tr>
			<td><br /></td>
		</tr>
		</table>
		</div>


<?php

	$time_count = count_time($queryExecutor, $selectionObj);
	$mapping_link = "time.php?step&&step_id=".$step_value['step_id']."";
	$title = "time corresponding entries.";
	$label = "Tim.";
	get_mapping_mark_up($time_count, $mapping_link, $title, $label);

	$workflowstepmap_count = count_workflowstepmap($queryExecutor, $selectionObj);
	$mapping_link = "workflowstepmap.php?step&&step_id=".$step_value['step_id']."";
	$title = "workflowstepmap corresponding entries.";
	$label = "Wor.";
	get_mapping_mark_up($workflowstepmap_count, $mapping_link, $title, $label);

	$steprolemap_count = count_steprolemap($queryExecutor, $selectionObj);
	$mapping_link = "steprolemap.php?step&&step_id=".$step_value['step_id']."";
	$title = "steprolemap corresponding entries.";
	$label = "Ste.";
	get_mapping_mark_up($steprolemap_count, $mapping_link, $title, $label);

	$userstepmap_count = count_userstepmap($queryExecutor, $selectionObj);
	$mapping_link = "userstepmap.php?step&&step_id=".$step_value['step_id']."";
	$title = "userstepmap corresponding entries.";
	$label = "Use.";
	get_mapping_mark_up($userstepmap_count, $mapping_link, $title, $label);



?>


	<label id="update_link_<?= $id_string ?>" onclick="showUpdate('update_<?= $id_string ?>');" style="cursor:pointer">
	<img src="images/icons/edit.png" width="15px" height="15px" title="edit entry" style="cursor:pointer" />
	</label> 
 &nbsp; 
	<?php 
		$link = "step.php?delete_Step&&step_id=".$step_value['step_id']."";
		$message = "";
	?>

	<?php showConfirmDeleteAction($id_string, $link, $message); ?>
	<label style="cursor:pointer" onclick="showDelete('delete_<?= $id_string ?>')">
	<img src="images/icons/delete.png" width="15px" height="15px" title="delete entry" />
	</label>
	</td>
<tr>
	<?php $i = ($i + 1); ?>
<?php endforeach; ?>
 <tr>
 <td colspan = "4"></td></tr></table>

<?php endif; ?>



<?php

function get_mapping_mark_up($entity_count, $mapping_link, $title, $label){

	if($entity_count > 0):

?>
		<a href="<?= $mapping_link ?>" target="_blank" title="<?= $title ?>" style="color: #000033; font-weight:bold;">
			<font size="-1"><?= $label ?></font>
		</a>
		&nbsp;
<?php
	endif;
}

?>