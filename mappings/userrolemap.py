<?php


if(isset($_GET['specific_user'])):


	$user_id = isset($_GET['user_id']) ? $fieldValidator->validate_field($_GET['user_id']) : "";

	$userrolemap_array = array();
	$role_array = array();
	$user_array = array();

	$query = $queryExecutor->execute($selectionObj->select_user($user_id));

	while($row = mysqli_fetch_array($query)):

		$user_id = $row['user_id'];
		$user_array[$user_id] = array();
		$user_array[$user_id]['user_id'] = $user_id;		$workspace_id = $row['workspace_id'];
		$user_array[$workspace_id] = array();
		$user_array[$workspace_id]['workspace_id'] = $workspace_id;

		$key = $user_id.$workspace_id.;

		$dependent_query = $queryExecutor->execute($selectionObj->select_user_first_name($user_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$user_array[$key]['first_name'] = $row_col['first_name'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_user_last_name($user_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$user_array[$key]['last_name'] = $row_col['last_name'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_user_email($user_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$user_array[$key]['email'] = $row_col['email'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_user_password($user_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$user_array[$key]['password'] = $row_col['password'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_user_job_title($user_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$user_array[$key]['job_title'] = $row_col['job_title'];


		$secondary_query = $queryExecutor->execute($selectionObj->select_userrolemap_by_user($user_id));

		while($sec_row = mysqli_fetch_array($secondary_query)):

			$role_id = $sec_row['role_id'];
			$role_array[$role_id] = array();
			$role_array[$role_id]['role_id'] = $role_id;

			$sec_key = $role_id;

			$dependent_query = $queryExecutor->execute($selectionObj->select_role_name($role_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$role_array[$sec_key]['name'] = $row_col['name'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_role_description($role_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$role_array[$sec_key]['description'] = $row_col['description'];

		endwhile;



	endwhile;


?>

<table cellspacing = "1" cellpadding = "0" align = "center" width = "100%" id = "userrolemap">
 <tr>
 <td colspan = "3">&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td colspan = "2"><a href="target_print.php?userrolemap&&user_id=<?= $user_id ?>" target="_blank" style="color:#00FF00;">Print PDF</a></td></tr>
 <tr class = "top_row">
 <td>&nbsp;&nbsp;#&nbsp;&nbsp;</td>
 <td>&nbsp;Role id&nbsp;</td>
 <td>&nbsp;Name&nbsp;</td>
 <td>&nbsp;Description&nbsp;</td>
 <td>&nbsp;&nbsp;Actions&nbsp;&nbsp;</td></tr>
 
<?php $i = 0; ?>


<?php  foreach($role_array as $role_key => $role_value): ?>
<?php $css_class = ($i+1)%2 == 0 ? "even_row" : "odd_row"; ?>


<tr>
	<td><?= ($i+1) ?></td>
	<td><?= $role_value['role_id'] ?></td>
	<td><?= $role_value['name'] ?></td>
	<td><?= $role_value['description'] ?></td>
	<td>

		<?php $id_string = $role_id; ?>

		<div id="update_role_<?= $id_string ?>" style="display:none" class="updates">
		<table border="0" align="center" class="overlay_contained_table">
		<tr>
			<td align="right">
			<div class="closebtn" id="close_circle" onclick="closeUpdateOverlay('update_role_<?= $id_string ?>');">&nbsp;&times;&nbsp;</div>
			</td>
		</tr>
		<tr><td><br /></td></tr>
		<tr>
			<td align="center">
			<fieldset style="width: 80%">
			<legend>role Information</legend>
			<?php update_role($queryExecutor, $selectionObj, $updateObj, $fieldValidator, $role_value['role_id']); ?>
			</fieldset>
			</td>
		</tr>
		<tr>
			<td><br /></td>
		</tr>
		</table>
		</div>


<?php

	$workspacerolemap_count = count_workspacerolemap($queryExecutor, $selectionObj);
	$mapping_link = "workspacerolemap.php?role&&role_id=".$role_value['role_id']."";
	$title = "workspacerolemap corresponding entries.";
	$label = "Wor.";
	get_mapping_mark_up($workspacerolemap_count, $mapping_link, $title, $label);

	$steprolemap_count = count_steprolemap($queryExecutor, $selectionObj);
	$mapping_link = "steprolemap.php?role&&role_id=".$role_value['role_id']."";
	$title = "steprolemap corresponding entries.";
	$label = "Ste.";
	get_mapping_mark_up($steprolemap_count, $mapping_link, $title, $label);

	$roleprivilegemap_count = count_roleprivilegemap($queryExecutor, $selectionObj);
	$mapping_link = "roleprivilegemap.php?role&&role_id=".$role_value['role_id']."";
	$title = "roleprivilegemap corresponding entries.";
	$label = "Rol.";
	get_mapping_mark_up($roleprivilegemap_count, $mapping_link, $title, $label);

	$userrolemap_count = count_userrolemap($queryExecutor, $selectionObj);
	$mapping_link = "userrolemap.php?role&&role_id=".$role_value['role_id']."";
	$title = "userrolemap corresponding entries.";
	$label = "Use.";
	get_mapping_mark_up($userrolemap_count, $mapping_link, $title, $label);



?>


	<label id="update_link_<?= $id_string ?>" onclick="showUpdate('update_<?= $id_string ?>');" style="cursor:pointer">
	<img src="images/icons/edit.png" width="15px" height="15px" title="edit entry" style="cursor:pointer" />
	</label> 
 &nbsp; 
	<?php 
		$link = "role.php?delete_Role&&role_id=".$role_value['role_id']."";
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
 <td colspan = "5"></td></tr></table>

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