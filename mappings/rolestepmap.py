<?php


if(isset($_GET['specific_role'])):


	$role_id = isset($_GET['role_id']) ? $fieldValidator->validate_field($_GET['role_id']) : "";

	$steprolemap_array = array();
	$role_array = array();
	$step_array = array();

	$query = $queryExecutor->execute($selectionObj->select_role($role_id));

	while($row = mysqli_fetch_array($query)):

		$role_id = $row['role_id'];
		$role_array[$role_id] = array();
		$role_array[$role_id]['role_id'] = $role_id;

		$key = $role_id;

		$dependent_query = $queryExecutor->execute($selectionObj->select_role_name($role_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$role_array[$key]['name'] = $row_col['name'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_role_description($role_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$role_array[$key]['description'] = $row_col['description'];


		$secondary_query = $queryExecutor->execute($selectionObj->select_steprolemap_by_role($role_id));

		while($sec_row = mysqli_fetch_array($secondary_query)):

			$step_id = $sec_row['step_id'];
			$step_array[$step_id] = array();
			$step_array[$step_id]['step_id'] = $step_id;

			$sec_key = $step_id;

			$dependent_query = $queryExecutor->execute($selectionObj->select_step_name($step_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$step_array[$sec_key]['name'] = $row_col['name'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_step_description($step_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$step_array[$sec_key]['description'] = $row_col['description'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_step_step_number($step_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$step_array[$sec_key]['step_number'] = $row_col['step_number'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_step_percentage($step_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$step_array[$sec_key]['percentage'] = $row_col['percentage'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_step_status($step_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$step_array[$sec_key]['status'] = $row_col['status'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_step_warning_threshold($step_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$step_array[$sec_key]['warning_threshold'] = $row_col['warning_threshold'];

		endwhile;



	endwhile;


?>

<table cellspacing = "1" cellpadding = "0" align = "center" width = "100%" id = "steprolemap">
 <tr>
 <td colspan = "8">&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td colspan = "2"><a href="target_print.php?steprolemap&&role_id=<?= $role_id ?>" target="_blank" style="color:#00FF00;">Print PDF</a></td></tr>
 <tr class = "top_row">
 <td>&nbsp;&nbsp;#&nbsp;&nbsp;</td>
 <td>&nbsp;Step id&nbsp;</td>
 <td>&nbsp;Name&nbsp;</td>
 <td>&nbsp;Description&nbsp;</td>
 <td>&nbsp;Step number&nbsp;</td>
 <td>&nbsp;Percentage&nbsp;</td>
 <td>&nbsp;Status&nbsp;</td>
 <td>&nbsp;Warning threshold&nbsp;</td>
 <td>&nbsp;Workflow id&nbsp;</td>
 <td>&nbsp;&nbsp;Actions&nbsp;&nbsp;</td></tr>
 
<?php $i = 0; ?>


<?php  foreach($step_array as $step_key => $step_value): ?>
<?php $css_class = ($i+1)%2 == 0 ? "even_row" : "odd_row"; ?>


<tr>
	<td><?= ($i+1) ?></td>
	<td><?= $step_value['step_id'] ?></td>
	<td><?= $step_value['name'] ?></td>
	<td><?= $step_value['description'] ?></td>
	<td><?= $step_value['step_number'] ?></td>
	<td><?= $step_value['percentage'] ?></td>
	<td><?= $step_value['status'] ?></td>
	<td><?= $step_value['warning_threshold'] ?></td>
	<td><?= $step_value['workflow_id'] ?></td>
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
 <td colspan = "10"></td></tr></table>

<?php endif; ?>

